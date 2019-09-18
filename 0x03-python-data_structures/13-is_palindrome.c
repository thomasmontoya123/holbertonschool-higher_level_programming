#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int buff[10000], i, j, size;
	listint_t *temporal;

	temporal = *head;

	j = 0;
	size = 0;

	if (!head || !(*head) || !(*head)->next)
		return (1);

	for (i = 0; temporal; i++, size++)
	{
		buff[size] = temporal->n;
		temporal = temporal->next;
	}

	for (i = size - 1; i >= 0 && j <= i; j++, i--)
	{
		if (buff[i] != buff[j])
			return (0);
	}

	return (1);
}
