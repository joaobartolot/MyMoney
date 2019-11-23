var homeApp = angular.module("HomeApp", []);

homeApp.controller("HomeController", ($scope, $http) => {
  $scope.owlCarouselConfig = {
    center: true,
    items: 2,
    loop: false,
    lazyLoad: true,
    margin: 10
    // responsive:{
    // 	0: {
    // 		center: true,
    // 		items:1
    // 	},
    // 	600: {
    // 		items:2
    // 	}
    // }
  };

  $scope.list = [];

  $http({
    method: "GET",
    url: "api/account-user-list"
  }).then(response => {
    $scope.list = response.data;
    console.log($scope.list);
    console.log(response.data);
  });
});
