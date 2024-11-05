#! /bin/sh

# Check if python is installed

MODULE_NAME="kaggle"

# Function to exit context
exiter() {
    local context="$1"
    echo "$context"
    read -p "Press enter to close terminal..."
    exit 0
}

if
    command -v python3 &
    >/dev/null
then
    echo "Python is installed"
    if
        python -c "import $MODULE_NAME" &
        >/dev/null
    then
        echo "Module $MODULE_NAME already installed."
    else
        echo "Module $MODULE_NAME not installed, do you want to install it ? [y/n]."

        # Read user input
        read -r user_input

        if [ "$user_input" = "y" ]; then
            # Attempt to install the module
            echo "Installing $MODULE_NAME..."
            pip install $MODULE_NAME
            if [ $? -eq 0 ]; then
                echo "$MODULE_NAME has been installed successfully."
            else
                exiter "Failed to install $MODULE_NAME. Please check your permissions or pip installation."
            fi
        else
            exiter "Installation skipped."
        fi
    fi
else
    exiter "Python not installed please install it before running this script."
fi

# Set the environment variable for Kaggle credentials
export KAGGLE_CONFIG_DIR=./kaggle_credentials

# Running python script
python ./data_processing/pull_data.py

read -p "Press enter to close terminal..."
