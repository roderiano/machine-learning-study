import numpy as np

input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = [0, 0, 0, 1]
weights = [0.0, 0.0]
learning_rate = 0.9

def sum(e, p):
    return e.dot(p)

def step_function(sum):
    if(sum >= 1):
        return 1
    else:
        return 0
    
def calculate_output(reg):
    s = sum(reg, weights)
    return step_function(s)

def learn():
    total_errors = 1

    while total_errors != 0:
        total_errors = 0

        for i in range(len(output)):
            temp_output = calculate_output(np.array(input[i]))
            error = abs(output[i] - temp_output)
            total_errors += error

            for j in range(len(weights)):
                weights[j] = weights[j] + (learning_rate * input[i][j] * error)
            
            print(f"updated weights: {weights}")

            if error == 0:
                output[i] = temp_output
        
        print(f"total errors: {total_errors}")
        
        
        print(f"input: {input}")
        print(f"output: {output}")

if __name__ == "__main__":
    learn()

