app.controller('addJob', function($scope,$http) {
    
    $scope.showRemotePath = false;
    $scope.showUseSSL = false;
    $scope.isLoading = false;
    
    $scope.changeType = function() {
        console.log($scope.type);
        console.log($scope.hostname);
        
        switch($scope.type) {
            case 'SSH':
            case 'SFTP':
            case 'FTP':
                $scope.showRemotePath = true;
                $scope.showUseSSL = false;
                break;
            default:
                $scope.showRemotePath = false;
                $scope.showUseSSL = false;
                break;
        }
    }
    
    $scope.createWebsite = function(){

        $scope.isLoading = true;
        
        switch($scope.type) {
            case 'SSH':
            case 'SFTP':
            case 'FTP':
                $scope.port = 0;
                $scope.useSSL = 'No';
                break;
            default:
                $scope.remotePath = 0;
                break;
        }

        url = "/backup/submitAddJob";

        var data = {
            name         : $scope.name,
            type         : $scope.type,
            email        : $scope.email,
            hostname     : $scope.hostname,
            username     : $scope.username,
            password     : $scope.password,
            port         : $scope.port,
            remotePath   : $scope.remotePath,
            useSSL       : $scope.useSSL
        };
        
        console.log(data);

        var config = {
            headers : {
                'X-CSRFToken': getCookie('csrftoken')
            }
        };

        $http.post(url, data,config).then(ListInitialDatas, cantLoadInitialDatas);


        function ListInitialDatas(response) {
            console.log(response)
            console.log("done")
            $scope.isLoading = false;
        }
        function cantLoadInitialDatas(response) {
            console.log(response)
            console.log("done")
            $scope.isLoading = false;
        }

    };

    
});
