# autodl

为autodl.com和codewithgpu.com准备的镜像

更新日志:

- 2024.5.5 初始化

## 镜像列表

| 镜像              | 用途                                                                                                                                         | 备注                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| ollama/base       | 安装ollama-v0.1.32<br />提供ollama_serve.ipynb，<br />ollama serve运行在6006端口，便于远程运行                                               | 基于miniconda/python3.10镜像                            |
| ollama/open-webui | 安装ollama+open-webui+cpolar<br />其中ollama serve运行在11434(未暴露)<br />open-webui运行在6006，<br />可根据需要使用cpolar暴露ollama server | 基于ollama/base<br />conda create -n webui python=3.11 |
