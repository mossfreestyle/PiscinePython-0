# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rwassim <rwassim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/17 16:01:02 by rwassim           #+#    #+#              #
#    Updated: 2025/12/17 16:12:11 by rwassim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime

seconde = time.time()

print(f"Seconds since January 1, 1970: {seconde:,.4f} or {seconde:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))