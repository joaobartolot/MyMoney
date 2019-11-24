function ModelAccount (account) {
	
}

angular
  .module("AccountListApp", [])
  .controller("AccountListController", function($scope, $http) {
    $scope.list = [];

    $scope.addNewAccount = () => {
      // Testing the add function (modify later)
      newItem = {
        $$hashKey: "object:17",
        id: 20,
        name: "Testing Angular",
        account_type: "CA",
        bank_name: "NU",
        card_name: "In SQL",
        initial_balance: "123",
        balance: "123",
        user: 1,
        cardImg: "Nubank.png"
      };

      $scope.list.push(newItem);
    };

    let url = "/api/account-user-list/";

    $http({
      method: "GET",
      url: url
    }).then(response => {
      let data = response.data;

      for (let item of data) {
				item.balanceView = 'R$ ' + item.balance.toString().slice(0, -2) + ',' + item.balance.toString().slice(-2)
        $scope.list.push(item);
      }
    });
  });
