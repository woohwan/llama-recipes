import fire
import os
from datasets import load_dataset

DATASET = "richard-park/aihub-contents-ko-only"

def main(split="validation", lang="ko", docs_to_sample=10_000, save_path="data"):
    dataset = load_dataset(DATASET, split=split, streaming=True)
    os.makedirs(save_path, exist_ok=True)
    with open(os.path.join(save_path, f"{lang}.txt"), "w") as f:
        count = 0
        for idx, d in enumerate(dataset):
            if idx % 10_000 == 0:
                print(f"Searched {idx} documents for {lang} documents. Found {count} documents.")
            if count >= docs_to_sample:
                break
            if d["langCode"] == lang:
                f.write(d["text"] + "\n")
                count += 1


if __name__ == "__main__":
    fire.Fire(main)