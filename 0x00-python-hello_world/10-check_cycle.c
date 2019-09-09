#include "lists.h"

/**
 * check_cycle - check for a loop of nodes
 * @list: list
 *
 * Return: 0 if no loop 1 if loop
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (fast && fast->next && slow && slow->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
