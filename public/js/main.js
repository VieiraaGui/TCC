const produtos = [
	{ id: 1, name: 'Notebook Lenovo', price: 1755.99},
	{ id: 2, name: 'Notebook Toshiba', price: 1000.99},
	{ id: 3, name: 'Notebook Asus', price: 3500.99},
	{ id: 4, name: 'Notebook Acer', price: 2000.99},
	{ id: 5, name: 'Memória RAM', price: 400.99},
	{ id: 6, name: 'HD', price: 399.99},
	{ id: 7, name: 'Cabo USB', price: 50.00},
	{ id: 8, name: 'Notebook da Xuxa', price: 100.00},
]


const inputPesquisa = $("#inputPesquisaProduto");
const btnPesquisa = $("#botaoPesquisa");

btnPesquisa.click(event => {
	event.preventDefault();
	const textoDigitado = inputPesquisa.val();
	const produtosFiltrados = produtos.filter(produto => produto.name.includes(textoDigitado)); 

	console.table(produtosFiltrados);


})





