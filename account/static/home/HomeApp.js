var homeApp = angular.module('HomeApp', []);

homeApp.controller('HomeController', ($scope, $http) => {

	$scope.owlCarouselConfig = {
		center: true,
		items: 2,
		loop: false,
		lazyLoad: true
		// responsive:{
		// 	0: {
		// 		center: true,
		// 		items:1
		// 	},
		// 	600: {
		// 		items:2
		// 	}
		// }
	}

  $scope.list = [];

  $http({
    method: 'GET',
    url: 'api/account-user-list',
  }).then(response => {
    $scope.list = response.data;
    console.log($scope.list);
    console.log(response.data);
  });
});

homeApp.directive("owlCarousel", function() {
    return {
        restrict: 'E',
        transclude: false,
        link: function(scope) {
            scope.initCarousel = function(element) {

                // provide any default options you want
                var defaultOptions = {};
                var customOptions = scope.$eval($(element).attr('data-options'));
                // combine the two options objects
                for (var key in customOptions) {
                    defaultOptions[key] = customOptions[key];
                }
                // init carousel
                var curOwl = $(element).data('owlCarousel');
                if (!angular.isDefined(curOwl)) {
                    $(element).owlCarousel(defaultOptions);
                }
                scope.cnt++;
            };
        }
    };
}).directive('owlCarouselItem', [
    function() {
        return {
            restrict: 'A',
            transclude: false,
            link: function(scope, element) {
                // wait for the last item in the ng-repeat then call init
                if (scope.$last) {
                    scope.initCarousel(element.parent());
                }
            }
        };
    }
]);
