#include "lists.h"

/**
 * check_cycle - a program that check if there is cycle in list
 * @list: the link to be checked
 * Return: 1 if the list has cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (1)
	{
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow)
				return (1);
		}
		else
			return (0);
	}
}
