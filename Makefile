# Variables
PROJECT_NAME = evnchw
PYTHON = python3
POETRY = poetry

# Default target
all: install kernel

# Install dependencies using Poetry
install:
	@echo "Installing dependencies..."
	$(POETRY) install

# Install Jupyter kernel for the Poetry environment
kernel:
	@echo "Installing Jupyter kernel..."
	$(POETRY) run pip install ipykernel
	$(POETRY) run $(PYTHON) -m ipykernel install --user --name=$(PROJECT_NAME) --display-name "Python ($(PROJECT_NAME))"

# Clean up the Jupyter kernels
clean-kernel:
	@echo "Cleaning up Jupyter kernel..."
	jupyter kernelspec uninstall $(PROJECT_NAME)

# Clean up the Poetry environment
clean:
	@echo "Cleaning up Poetry environment..."
	$(POETRY) env remove

# .PHONY targets
.PHONY: all install kernel clean-kernel clean
