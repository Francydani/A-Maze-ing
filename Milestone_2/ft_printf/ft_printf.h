/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: francysa <francysa@student.42urduliz.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/15 11:35:01 by francysa          #+#    #+#             */
/*   Updated: 2026/05/25 10:44:07 by francysa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdlib.h>
# include <stdarg.h>

int	ft_printf(char const *str, ...);
int	ft_putnum_hex(unsigned long long num, char *base);
int	ft_putstr_len(char *s);
int	ft_putchar_len(char c);
int	ft_int(int num);

#endif