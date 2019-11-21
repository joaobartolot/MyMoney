var homeApp = angular.module('HomeApp', []);

homeApp.controller('HomeController', ($scope, $http) => {
  let self = $scope;

  self.list = [];

  $http({
    method: 'GET',
    url: 'api/account-user-list',
  }).then(response => {
    self.list = response.data;
    console.log(self.list);
    console.log(response.data);
  });
});
console.log(myGlide.index)
