from engine import Model

model = Model('gpt2')

print(model)

with model.invoke('Hello world') as invoker:
    
    zzz = model.transformer.h[2].output.copy()

output = model(device_map='auto')

breakpoint()
