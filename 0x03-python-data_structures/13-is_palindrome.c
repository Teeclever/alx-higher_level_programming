#include "lists.h"

/**
 * rev_listint - Function to reverse a linked list in place.
 * @h: Pointer to the pointer of the first node in the list.
 */
void rev_listint(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *current = *h;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*h = prev;
}

/**
 * is_palindrome - a function tht Checks if a list is a palindrome.
 * @head: Double pointer to the linked list.
 * Return: 1 if it is a palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	rev_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	
	if (!dup)
		return (1);
	return (0);
}
