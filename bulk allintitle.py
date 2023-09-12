import requests
import os
import time
import pandas as pd


# Define your Google API key and Custom Search Engine ID here
GOOGLE_API_KEY = "YOUR_API_KEY"
CSE_ID = "YOUR_CSE_ID"


# Maximum number of requests per minute to stay within Google's limits
MAX_REQUESTS_PER_MINUTE = 60
# Time interval (in seconds) to wait between requests
REQUEST_INTERVAL = 60 / MAX_REQUESTS_PER_MINUTE

# Maximum number of retry attempts for a single request
MAX_RETRY_ATTEMPTS = 3

# Get the directory of the script file
script_directory = os.path.dirname(__file__)

# Specify the output directory as the script directory
output_directory = script_directory
output_filename = "allintitle_results.xlsx"  # Updated output filename

def search_allintitle_with_retry(keyword, df, row_index):
    for attempt in range(MAX_RETRY_ATTEMPTS):
        try:
            # Define the Google Custom Search JSON API endpoint
            base_url = "https://www.googleapis.com/customsearch/v1"
            
            # Construct the query parameters with "allintitle:"
            params = {
                "q": f'allintitle:{keyword}',
                "key": GOOGLE_API_KEY,
                "cx": CSE_ID,
            }
            
            # Send a GET request to the Google Custom Search API
            response = requests.get(base_url, params=params)
            
            # Check if the request was successful
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()
            
            # Get the total number of search results
            total_results = data.get('searchInformation', {}).get('totalResults', 0)

            # Add the results to the DataFrame at the specified row index
            df.at[row_index, "Keyword"] = keyword
            df.at[row_index, "Allintitle Results"] = total_results

            # Construct the full output file path in the script directory
            output_file_path = os.path.join(output_directory, output_filename)

            # Save the DataFrame to an Excel file in the script directory
            df.to_excel(output_file_path, index=False)
            print(f"Results saved to {output_file_path}")

            return

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < MAX_RETRY_ATTEMPTS - 1:
                print("Retrying after a delay...")
                time.sleep(5)  # Add a delay before retrying
            else:
                print(f"Failed to retrieve results for '{keyword}'.")
                return

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            return

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

if __name__ == "__main__":
    # Prompt the user for the input file path
    input_file_path = input("Enter the path of the TXT file containing keywords: ")

    # Read keywords from the input file
    with open(input_file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines()]

    if not keywords:
        print("No keywords found in the input file. Exiting...")
    else:
        # Create an empty DataFrame to store the results
        df = pd.DataFrame(columns=["Keyword", "Allintitle Results"])

        for i, keyword in enumerate(keywords):
            search_allintitle_with_retry(keyword, df, i)
            time.sleep(REQUEST_INTERVAL)  # Wait before the next request to comply with rate limits

        print("All queries completed.")
