import subprocess
import concurrent.futures

# The bash script to run
bash_script = "new_bash.sh"

# Function to execute the bash script with a parameter
def run_bash_script(param):
    print("Running: {bash_script} with parameter {param}")
    try:
        # Pass the parameter to the bash script
        process = subprocess.Popen(['bash', bash_script, str(param)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()  # Capture output and error
        return_code = process.returncode
        if return_code == 0:
            print("Finished: {bash_script} with parameter {param}")
        else:
            print("Error in {bash_script} with parameter {param}: {stderr.decode('utf-8')}")
        return return_code
    except Exception as e:
        print("Exception while running {bash_script} with parameter {param}: {e}")
        return None

# Max number of concurrent scripts
MAX_CONCURRENT = 7

# Number of times to run the script (432 times)
TOTAL_RUNS = 432

# Using ThreadPoolExecutor to manage concurrent processes
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT) as executor:
    # Submit the same bash script 432 times with different parameters
    futures = {executor.submit(run_bash_script, i): i for i in range(TOTAL_RUNS)}
    
    # Wait for all the scripts to finish
    for future in concurrent.futures.as_completed(futures):
        param = futures[future]
        try:
            result = future.result()  # Retrieve the result of the script
            if result is not None:
                print("Script with parameter {param} completed with return code {result}")
        except Exception as e:
            print("Script with parameter {param} generated an exception: {e}")
