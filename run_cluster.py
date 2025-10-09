# run_cluster.py
from pathlib import Path
from code_clustering_pipeline import Config, run

SRC_DIR = r"D:\GitHub\dolap\files_dolab\files"
OUT_DIR = r"D:\GitHub\dolap\files_dolab\out_file"

cfg = Config(
    src=Path(SRC_DIR),
    out_dir=Path(OUT_DIR),

    # ล็อค k ที่ได้จาก auto-k รอบก่อน
    use_auto_k=False,
    k=12,

    # กรอง/เสถียรภาพ
    max_files=9000,
    min_lines=5,          # เดิม 3 → เพิ่มเป็น 5 ช่วยลดไฟล์รบกวน
    batch_size=2,
    device="cpu",

    # ทำความสะอาด (คงไว้ดีแล้ว)
    strip_docs_comments=True,
    ast_rename_identifiers=True,
    squeeze_whitespace=True,

    # เผื่อ fallback เป็น TF-IDF (จะลดมิติให้ก่อน KMeans)
    svd_components=256,

    # บันทึก embedding ไว้ใช้ต่อ (เช่นทำ visualization อื่นๆ)
    # save_embeddings=Path(OUT_DIR) / "embeddings.npy",
)
run(cfg)
print("DONE. ดูผลได้ใน:", OUT_DIR)
