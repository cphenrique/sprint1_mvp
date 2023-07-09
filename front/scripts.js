/*
  --------------------------------------------------------------------------------------
  Função para obter a lista de projetos existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/projetos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.projetos.forEach(projeto => insertList(projeto.nome, projeto.descricao, projeto.inicio, projeto.fim, projeto.categoria, projeto.gerente, projeto.status))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()


/*
  --------------------------------------------------------------------------------------
  Função para colocar um projeto no servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputProjeto, inputDescricao, inputInicio, inputFim, inputCategoria, inputGerente, inputStatus) => {
  const formData = new FormData();
  formData.append('nome', inputProjeto);
  formData.append('descricao', inputDescricao);
  formData.append('inicio', inputInicio);
  formData.append('fim', inputFim);
  formData.append('id_categoria', inputCategoria);
  formData.append('id_gerente', inputGerente);
  formData.append('id_status', inputStatus);

  let url = 'http://127.0.0.1:5000/projeto';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let btn = document.createElement("button");
  let txt = document.createTextNode("del");
  btn.className = "btn btn-danger";
  btn.appendChild(txt);
  parent.appendChild(btn);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("btn-danger");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um projeto do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/projeto?nome=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo projeto
  --------------------------------------------------------------------------------------
*/
const newItem = () => {
  let inputProjeto = document.getElementById("newProjeto").value;
  let inputDescricao = document.getElementById("newDescricao").value;
  let inputInicio = document.getElementById("newInicio").value;
  let inputFim = document.getElementById("newFim").value;
  let inputCategoria = document.getElementById("newCategoria").value;
  let inputGerente = document.getElementById("newGerente").value;
  let inputStatus = document.getElementById("newStatus").value;

  if (inputProjeto === '') {
    alert("O nome do Projeto é obrigatório");
  } else {
    insertList(inputProjeto, inputDescricao, inputInicio, inputFim, inputCategoria, inputGerente, inputStatus)
    postItem(inputProjeto, inputDescricao, inputInicio, inputFim, inputCategoria, inputGerente, inputStatus)
    alert("Projeto adicionado!")
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para inserir projetos na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (nome, descricao, inicio, fim, categoria, gerente, status) => {
  var item = [nome, descricao, inicio, fim, categoria, gerente, status]
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("newProjeto").value = "";
  document.getElementById("newDescricao").value = "";
  document.getElementById("newInicio").value = "";
  document.getElementById("newFim").value = "";
  document.getElementById("newCategoria").value = "";
  document.getElementById("newGerente").value = "";
  document.getElementById("newStatus").value = "";

  removeElement()
}

/*
  --------------------------------------------------------------------------------------
  Função para popular combobox com os dados de categoria do projeto
  --------------------------------------------------------------------------------------
*/
const getListCategorias = async () => {
  let url = 'http://127.0.0.1:5000/categorias';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.categorias.forEach(categoria => insertListCategorias(categoria.id_categoria, categoria.categoria))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertListCategorias = (id, categoria) => {

  var combobox = document.getElementById('newCategoria');
  var option = document.createElement("option");
  option.value = id;
  option.text = categoria;
  combobox.add(option);
  combobox.selectedIndex = 0;

}

getListCategorias()

/*
  --------------------------------------------------------------------------------------
  Função para popular combobox com os gerentes dos projetos
  --------------------------------------------------------------------------------------
*/

const getListGerentes = async () => {
  let url = 'http://127.0.0.1:5000/gerentes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.gerentes.forEach(gerente => insertListGerentes(gerente.id_gerente, gerente.gerente))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertListGerentes = (id, gerente) => {

  var combobox = document.getElementById('newGerente');
  var option = document.createElement("option");
  option.value = id;
  option.text = gerente;
  combobox.add(option);
  combobox.selectedIndex = 0;

}

getListGerentes()

/*
  --------------------------------------------------------------------------------------
  Função para popular combobox com os statuses dos projetos
  --------------------------------------------------------------------------------------
*/

const getListStatuses = async () => {
  let url = 'http://127.0.0.1:5000/statuses';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.statuses.forEach(status => insertListStatuses(status.id_status, status.status))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const insertListStatuses = (id, status) => {

  var combobox = document.getElementById('newStatus');
  var option = document.createElement("option");
  option.value = id;
  option.text = status;
  combobox.add(option);
  combobox.selectedIndex = 0;

}

getListStatuses()
