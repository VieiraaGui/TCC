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




function addIconClasses() {
    $(".Promocoes-Produto").each(function(){
        const scre = $("body").width();
        const prom = $(".Promocoes-Produto");
		const divProm = $(".prom-prod");
        if ( scre <= 991 ) {
            prom.addClass("container-fluid");
            prom.removeClass("container");
            divProm.addClass('col-md-12');
            divProm.removeClass('col-md-9');
        } if ( scre > 991 ) {
            prom.addClass('container');
            prom.removeClass('container-fluid');
            divProm.addClass('col-md-9');
            divProm.removeClass('col-md-12');
        } 

        if (prom.hasClass('container-fluid')){
        		const divProm = $(".prom-prod");
        		const btnIcone = $("#icone-responsive, #icone-responsive path");
				btnIcone.click(event => {
				const iToggle = $(event.target);

				let isToggled = 'true';

				if (iToggle.attr('fill')) 
					isToggled = iToggle.closest('svg').attr('data-toggle');
				
			    else 
					isToggled = iToggle.attr('data-toggle');
				
				if (isToggled === "false") {
					divProm.removeClass('col-sm-12');
					divProm.addClass('col-sm-9');
					iToggle.attr('data-toggle', 'true');
					divProm.addClass('col-md-9');
					divProm.removeClass('col-md-12');
					$(".hidden").css("background-color", 'white');
					$(".icone").css("color", 'black');

				} else {
					divProm.removeClass('col-sm-9');
					divProm.addClass('col-sm-12');
					iToggle.attr('data-toggle', 'false');
					divProm.addClass('col-md-12');
					divProm.removeClass('col-md-9');
					$(".hidden").css("background-color", 'transparent');
					$(".icone").css("color", 'white');
				}

			});
        }
    });

}


$(document).ready(function () {
    addIconClasses();
    $(window).resize(function() {
        addIconClasses();
    });
});


//	$(function() {
//   $(document).ready(function() {
//
//            $("#geraPc").click(function(event){
//                $.getJSON('Comp.json', function(emp) {
//                    $('#Processador').html('<p> Name: ' utilidade + '</p>');
//
//                });
//            });
//        });
//});

 $(document).ready(function() {

            $("#geraPc").click(function(event){
                $.get('/static/arquivo.txt', function(emp) {
                    $('#Processador').html('<p> Utilidade: '  + emp +  '</p>');
                    $('#Processador').append('<p> Teste: '  + emp +  '</p>');
                });
            });
        });

/*const btnIcone = $("#icone-responsive");
	btnIcone.click(event => {
	const iToggle = $(event.target);
	const isToggled = iToggle.attr('data-toggle');
	const divProm = $("#div-prom");
	const scre = $("body").width();

	if (isToggled === "false") && (scre > 991) {
		divProm.removeClass('col-sm-12');
		divProm.addClass('col-sm-9');
		iToggle.attr('data-toggle', 'true');
	} else {
		divProm.removeClass('col-sm-9');
		divProm.addClass('col-sm-12');
		iToggle.attr('data-toggle', 'false');
	}
});*/

