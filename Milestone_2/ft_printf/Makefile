# **************************************************************************** #
#                                                                              #
#                                                          :::      ::::::::   #
#   Makefile                                             :+:      :+:    :+:   #
#                                                      +:+ +:+         +:+     #
#   By: francysa <francysa@student.42urduliz.com>    +#+  +:+       +#+        #
#                                                  +#+#+#+#+#+   +#+           #
#   Created: 2026/05/15 11:38:49 by francysa            #+#    #+#             #
#   Updated: 2026/05/25 10:37:12 by francysa           ###   ########.fr       #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a

CC = gcc
CFLAGS = -Wall -Wextra -Werror

UTILS = ft_printf_utils.c 

SRC = ft_printf.c $(UTILS)
OBJ = $(SRC:.c=.o)

INCLUDE = ft_printf.h

AR = ar rcs
RM = rm -f

.PHONY: all clean fclean re

all: $(NAME)

$(NAME): $(OBJ)
		$(AR) $@ $^

%.o: %.c $(INCLUDE)
		$(CC) $(CFLAGS) -c -o $@ $<

clean:
		$(RM) $(OBJ) $(OBJ_BONUS)
		
fclean: clean
		$(RM) $(NAME) libftprintf.h.gch

re: fclean all