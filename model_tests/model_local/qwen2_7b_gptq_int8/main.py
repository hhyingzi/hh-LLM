import os
from modelscope import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline
from modelscope.utils.constant import Tasks

model_path = r"/mnt/workspace/model/Qwen2-7B-Instruct-GPTQ-Int8"
device = "cuda" # cpu, cuda, cuda:0

def model_downloader():
    os.environ['HF_ENDPOINT'] = "https://hf-mirror.com/"
    # 通过hfd工具下载模型
    # ./hfd.sh Qwen/Qwen2-7B-Instruct-GPTQ-Int8 --tool aria2c -x 4 -d /mnt/workspace/model/Qwen2-7b-gptq-int8

def load_local_model():
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype="auto",
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

def infer_from_scratch():
    model, tokenizer = load_local_model()

    prompt = "香蕉是什么颜色的？"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(response)

def infer_from_pipeline():
    generator = pipeline(Tasks.text_generation, model=model, tokenizer=tokenizer)
    result = generator(messages, max_length=50)[0]['generated_text']
    print(result)

if __name__ == "__main__":
    load_local_model()
    infer_from_scratch()