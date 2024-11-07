#! /bin/sh

MODULE_NAME="kaggle"

# Function to exit context
exiter() {
    local context="$1"
    echo "$context"
    read -p "Press enter to close terminal..."
    exit 0
}

# Check if python is installed

if type -P python >/dev/null 2>&1 || type -P python3 >/dev/null 2>&1; then
    echo "Python is installed"
else
    exiter "Python is not installed"
fi

# Check if kaggle module is installed

if python -c "import $MODULE_NAME" >/dev/null 2>&1; then
    echo "Module '$MODULE_NAME' is already installed."
else
    echo "Module '$MODULE_NAME' is not installed, do you want to install it [y/n]?"
    read -r user_input

    if [ "$user_input" == "y" ]; then
        # Install the module
        echo "Installing $MODULE_NAME..."
        pip install $MODULE_NAME

        if [ $? -eq 0 ]; then
            echo "$MODULE_NAME has been installed successfully."
        else
            exiter "Failed to install $MODULE_NAME, please check your permissions or pip installation."
        fi
    else
        exiter "Installation skipped"
    fi
fi

echo "Pulling data..."
python ./data_processing/pull_data.py
exiter "Data pulled."
