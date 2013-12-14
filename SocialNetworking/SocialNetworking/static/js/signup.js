'use strict';
angular.module('sign_up_app', ['ui.bootstrap'])
    .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
    ])
    .config(['$interpolateProvider',function($interpolateProvider){
        $interpolateProvider.startSymbol('//');
        $interpolateProvider.endSymbol('//');
    }])
  .controller('SignupController', function($scope, $http) {


//        $scope.$watch('username',function(){
//
//                $http.post('/check_username/',{"username":$scope.username})
//                    .success(function(data) {
//               // alert("D" + data.isValid);
//                       //$scope.username.$setValidity("us",data.isValid);
//                       $scope.username.$setValidity("isUnqiue", data.isValid)
//
//
//                    })
//                    .error(function(data) {
//                        $scope.username.$setValidity("isUnqiue",false);
//                    })
//
//         });
//
//        $scope.$watch('email',function(){
//
//                $http.post('/check_email/',{"email":$scope.email})
//                    .success(function(data) {
//                         $scope.email.$setValidity("el",data.isValid);
//                    })
//                    .error(function(data) {
//                        $scope.email.$setValidity("el",false);
//                    })
//
//        });

  })
//.directive('isUnique', function() {
//  return {
//    require: 'ngModel',
//    link: function(scope, elm, attrs, ctrl) {
//      ctrl.$parsers.unshift(function(viewValue) {
//
//          // it is valid
//          ctrl.$setValidity('isUnique', true);
//          return viewValue;
//
//      });
//    }
//  };
//})






//.directive('isUnique', function ($http) {
//         return function (scope, elm, attrs, ctrl) {
//
//            scope.watch("username",function(value) {
//                $http.post('/check_username/', {"username":value})
//                .success(function (data) {
//                     alert(data);
//                 })
//                 .error(function(data) {
//                     alert(data);
//                 })
//            })
//         }
//    });

//.directive("isUnqiue", function(){
//    return {
//        require:"ngModel",
//        link: function(scope, element, attr, ngModel){
//                scope.$watch(function(){
//                    return ngModel.$modelValue;
//                }, function(modelValue){
//                    //ajax
//                });
//            }
//    }
//});

