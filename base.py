import os
import asyncio

# 设置运行端口
os.environ.update({'OLLAMA_HOST': '0.0.0.0:6006'})

async def run_process(cmd, verb=True, path=None):
  if path:
    os.chdir(path)
  print(f'>>> starting {path}:', *cmd)
  p = await asyncio.subprocess.create_subprocess_exec(
      *cmd,
      stdout=asyncio.subprocess.PIPE,
      stderr=asyncio.subprocess.PIPE,
  )


  async def pipe(lines):
    async for line in lines:
      print(line.strip().decode('utf-8'))

  if verb:
      await asyncio.gather(
          pipe(p.stdout),
          pipe(p.stderr),
      )
  else:
    await asyncio.gather(pipe(p.stdout))

await asyncio.gather(
    run_process(['ollama', 'serve']),
)
