def load_conversations():
    id2line = {}
    with open(path_to_movie_lines, errors='ignore') as f:
    lines = f.readlines()

    for line in lines:
        line = line.replace("\n","")
        parts = line.split(" +++$+++ ")
        id2line[parts[0]] = parts[4]
    inputs, outputs = [], []
    with open(path_to_movie_conversations, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.replace("\n","")
        parts = line.split(" +++$+++ ")
        conversation = [line[1:-1] for line in parts[3][1:-1].split(", ")]

        for i in range(len(conversation)-1):
            inputs.append(preprocess_sentence(id2line[conversation[i]]))
            outputs.append(preprocess_sentence(id2line[conversation[i+1]]))
            if len(inputs) >= MAX_SAMPLES:
                return inputs, outputs
    return inputs, outputs