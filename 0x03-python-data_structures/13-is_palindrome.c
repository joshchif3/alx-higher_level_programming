#include "lists.h"

/**
 * palindrome - gets from is_palindrome
 * @top:to get top
 * @next:to go next
 * Return:
 */
int palindrome(listint_t **top, listint_t *next)
{
int result = 0;

if (next == NULL)
	return (1);

if (palindrome(top, next->next) && ((*top)->n == next->n))
	result = 1;

*top = (*top)->next;

return (result);
}

/**
 * is_palindrome - for checking
 * @head: the top file
 * Return: required or bring 0
 */
int is_palindrome(listint_t **head)
{
	return (palindrome(head, *head));
}
