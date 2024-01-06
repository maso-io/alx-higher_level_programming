#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
 * insert_node - inserts node into listint_t singly linked list
 * @head: pointer to location of head node
 * @number: value of node to insert
 *
 * Return: memory location of new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;
	int n_val; /* next value */

	current = *head;
	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	while (current != NULL)
	{
		if (number < current->n)
		{
			new->next = current;
			new->n = number;
			*head = new;

			return (new);
		}
		if (current->next == NULL && number > current->n)
		{
			current->next = new;
			new->next = NULL;
			new->n = number;

			return (new);
		}
		n_val = (current->next)->n;
		if (current->n < number && n_val > number)
		{
			new->next = current->next;
			current->next = new;
			new->n = number;

			return (new);
		}
		current = current->next;
	}

	return (NULL);
}
