# -*- coding: utf-8 -*-
import json
import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def select_and_extract_messages():
    """
    Opens a file dialog for the user to select an Instagram 'message_1.json' file,
    parses the message history, fixes encoding issues, and exports a clean,
    chronological timestamped text log.
    """
    # Initialize hidden tkinter root window for file dialogs
    root = tk.Tk()
    root.withdraw()
    
    # Prompt user to select the target JSON file
    input_file = filedialog.askopenfilename(
        title="Select Instagram 'message_1.json' File",
        filetypes=[("JSON Files", "*.json")]
    )
    
    if not input_file:
        print("Operation cancelled by user.")
        return

    # Set the output text log path in the same directory as the input file
    directory = os.path.dirname(input_file)
    output_file = os.path.join(directory, 'clean_timestamped_log.txt')
        
    try:
        # Load and parse the JSON message data
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        formatted_messages = []
        messages = data.get('messages', [])
        
        # Fallback if the root JSON structure is a direct list of messages
        if not messages and isinstance(data, list):
            messages = data
            
        # Reverse the list to achieve chronological order (oldest to newest)
        messages.reverse()
        
        for msg in messages:
            # Extract sender name and message content with fallback keys
            sender = msg.get('sender_name', msg.get('author', {}).get('name', 'Unknown'))
            content = msg.get('content', msg.get('text', ''))
            timestamp_ms = msg.get('timestamp_ms', 0)
            
            # Convert millisecond timestamp to readable format [DD.MM.YY - HH:MM]
            timestamp_text = ""
            if timestamp_ms:
                dt_obj = datetime.datetime.fromtimestamp(timestamp_ms / 1000.0)
                timestamp_text = dt_obj.strftime("[%d.%m.%y - %H:%M]")
            else:
                timestamp_text = "[No Timestamp]"
            
            # Fix potential Instagram Latin1/UTF-8 character encoding discrepancies
            if content:
                try:
                    content = content.encode('latin1').decode('utf-8')
                except Exception:
                    pass
                try:
                    sender = sender.encode('latin1').decode('utf-8')
                except Exception:
                    pass
                    
            if content:
                # Format: [15.06.26 - 04.44] [Sender]: Message content
                formatted_messages.append(f"{timestamp_text} [{sender}]: {content}")
                
        # Write the processed messages to the output text file
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write('\n'.join(formatted_messages))
            
        messagebox.showinfo("Success!", f"Messages successfully extracted!\nOutput file generated at:\n{output_file}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during execution:\n{str(e)}")

if __name__ == '__main__':
    select_and_extract_messages()