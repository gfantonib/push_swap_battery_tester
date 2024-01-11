#include <stdlib.h>
#include <stdio.h>

typedef struct s_stack
{
	int	index;
	struct s_stack *next;
}		t_stack;

t_stack	*stack_new(int index);
void	stack_add_bottom(t_stack **stack, t_stack *new);
t_stack	*get_stack_bottom(t_stack *stack);
void	print_stack(t_stack **stack);
static void	push(t_stack **src, t_stack **dest);

int	main(void)
{
	t_stack	*stack_a;
	t_stack	*stack_b;

	stack_a = stack_new(2);
	stack_b = stack_new(3);

	stack_add_bottom(&stack_a, stack_new(4));
	stack_add_bottom(&stack_a, stack_new(6));
	stack_add_bottom(&stack_a, stack_new(8));

	stack_add_bottom(&stack_b, stack_new(5));
	stack_add_bottom(&stack_b, stack_new(7));
	stack_add_bottom(&stack_b, stack_new(9));

	printf("before\n");
	print_stack(&stack_a);
	print_stack(&stack_b);
	printf("\n");

	push(&stack_a, &stack_b);

	printf("after\n");
	print_stack(&stack_a);
	print_stack(&stack_b);
}

t_stack	*stack_new(int index)
{
	t_stack	*new;

	new = malloc(sizeof * new);
	if (!new)
		return (NULL);
	new->index = index;
	return (new);
}

void	stack_add_bottom(t_stack **stack, t_stack *new)
{
	t_stack	*tail;

	if (!new)
		return ;
	if (!*stack)
	{
		*stack = new;
		return ;
	}
	tail = get_stack_bottom(*stack);
	tail->next = new;
}

t_stack	*get_stack_bottom(t_stack *stack)
{
	while (stack && stack->next != NULL)
		stack = stack->next;
	return (stack);
}

void	print_stack(t_stack **stack)
{
	t_stack *current;

	current = *stack;
	while (current)
	{
		printf("%d|", current->index);
		printf("%p --> ", current);
		current = current->next;
	}
	printf("\n");
}

static void	push(t_stack **src, t_stack **dest)
{
	t_stack	*tmp;

	if (*src == NULL)
		return ;
	tmp = (*src)->next;
	(*src)->next = *dest;
	*dest = *src;
	*src = tmp;
}