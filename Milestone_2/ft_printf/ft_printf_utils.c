/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: francysa <francysa@student.42urduliz.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 10:14:15 by francysa          #+#    #+#             */
/*   Updated: 2026/05/25 10:44:43 by francysa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static size_t	ft_strlen(const char *s)
{
	size_t	count;

	count = 0;
	while (s[count])
		count++;
	return (count);
}

int	ft_putnum_hex(unsigned long long num, char *base)
{
	int	count;

	count = 0;
	if (num >= 16)
		count += ft_putnum_hex(num / 16, base);
	write (1, &base[num % 16], 1);
	count++;
	return (count);
}

int	ft_putstr_len(char *s)
{
	int	len;

	if (!s)
	{
		write(1, "(null)", 6);
		return (6);
	}
	len = ft_strlen(s);
	write(1, s, len);
	return (len);
}

int	ft_putchar_len(char c)
{
	write(1, &c, 1);
	return (1);
}
