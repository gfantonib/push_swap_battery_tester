// Assignment name  : ft_split
// Expected files   : ft_split.c
// Allowed functions: malloc
// --------------------------------------------------------------------------------

// Write a function that takes a string, splits it into words, and returns them as
// a NULL-terminated array of strings.

// A "word" is defined as a part of a string delimited either by spaces/tabs/new
// lines, or by the start/end of the string.

// Your function must be declared as follows:

// char    **ft_split(char *str);

#include <stdio.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int i = 0;
	while (str[i])
		i++;
	return (i);
}

int	ft_count_words(char *str)
{
	int	len;
	int	i;

	len = 0;
	i = 0;
	while (str[i])
	{
		while (str[i] == ' ')
			i++;
		if (str[i])
			len++;
		while (str[i] != ' ' && str[i] != '\0')
			i++;

	}
	return (len);
}

void	ft_putnstr(char *dest, char *src, int start)
{
	int i;

	i = 0;
	while (src[start] && src[start] != ' ')
	{
		dest[i] = src[start];
		i++;
		start++;
	}
	dest[i] = '\0';

}

char    **ft_split(char *str)
{
	char	**str_array;
	int		len;
	int		i;
	int		j;

	len = ft_count_words(str);
	str_array = malloc((sizeof(char *) * len) + 1);
	if (!str_array)
		return (NULL);
	str_array[len] = NULL;

	len = 0;
	i = 0;
	j = 0;
	while (str[i])
	{
		while (str[i] == ' ')
			i++;
		j = i;
		while (str[i] != ' ' && str[i])
			i++;
		if (i > j)
		{
			str_array[len] = malloc((sizeof(char) * (i - j) + 1));
			ft_putnstr(str_array[len], str, j);
		}
		len++;
	}
	return (str_array);

}

int	main(int argc, char **argv)
{
	char	**str_array = NULL;
	int	i;

	if (argc != 2)
		return (1);
	str_array = ft_split(argv[1]);
	i = 0;
	while (str_array[i])
	//&& ft_strlen(str_array[i]))
	{
		printf("%s\n", str_array[i]);
		i++;
	}
	return (0);
}