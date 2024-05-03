import pathlib

from datatrove.pipeline.readers import IpcReader
from datatrove.executor import LocalPipelineExecutor
from datatrove.data import DocumentsPipeline
from langdetect import detect_langs
from datatrove.data import Document
from datatrove.pipeline.filters.base_filter import BaseFilter
from datatrove.pipeline.writers.disk_base import DiskWriter
from datatrove.pipeline.writers.jsonl import JsonlWriter


DATA_DIR = "/mnt/nlpdata1/share/datasets/allenai___c4/tr/0.0.0/1588ec454efa1a09f29cd18ddd04fe05fc8653a2"
DUMP_DATA_DIR = "/mnt/nlpdata1/home/ismayilz/morph-gen-c4"

def preprocessing_adapter(document: Document, source_file: str, id_in_file: str = None) -> DocumentsPipeline:
    return {
        "id": id_in_file,
        "text": document["text"].lower(),
        "metadata": {
            "url": document["url"],
            "timestamp": str(document["timestamp"]),
            "file_stem": pathlib.Path(source_file).stem
        }
    }

class TRLanguageFilter(BaseFilter):
    name = "🌍 Language ID"
    _requires_dependencies = ["langdetect"]

    def __init__(
        self,
        language_threshold: float = 0.9,
        exclusion_writer: DiskWriter = None,
    ):
        super().__init__(exclusion_writer)
        self.language_threshold = language_threshold
        self._model = None

    def filter(self, doc: Document) -> bool:
        tr_score = 0

        try:
            lang_scores = detect_langs(doc.text)

            for lang_score in lang_scores:
                if lang_score.lang == "tr":
                    tr_score = float(lang_score.prob)
        except Exception as e:
            pass
        
        doc.metadata["tr_score"] = tr_score
        return tr_score > self.language_threshold
    
preprocessing = LocalPipelineExecutor(
    pipeline=[
        IpcReader(DATA_DIR, stream=True, progress=True, glob_pattern="*.arrow", adapter=preprocessing_adapter),
        TRLanguageFilter(exclusion_writer=JsonlWriter(f"{DUMP_DATA_DIR}/lang_filter_removed", "${file_stem}_${rank}.jsonl")),
        JsonlWriter(f"{DUMP_DATA_DIR}/lang_filtered", "${file_stem}_${rank}.jsonl")
    ],
    logging_dir=f"{DUMP_DATA_DIR}/logs/",
    tasks=600,
    workers=64
)

if __name__ == "__main__":
    preprocessing.run()