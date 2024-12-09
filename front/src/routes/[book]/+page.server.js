import * as Book from "$lib/books";

export async function load({ params }) {
  const book = await Book.get_a_book(params.book);
  return book;
}

export const actions = {
  default: async ({ request, cookies }) => {
    const data = await request.formData();
    console.log(data);
  },
};
