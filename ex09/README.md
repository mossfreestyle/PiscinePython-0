# ft_package

A simple test package.

## Installation

You can install the package via pip (assuming you have built the distribution):

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

Here is an example of how to use the `count_in_list` function from the package:

```python
from ft_package import count_in_list

lst = ["toto", "tata", "toto"]
print(count_in_list(lst, "toto"))  # Output: 2
print(count_in_list(lst, "tutu"))  # Output: 0
```

## License

This project is licensed under the MIT License.
