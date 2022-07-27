var data = {
    resource_id: 'e83f763b-b7d7-479e-b172-ae981ddc6de5', // the resource id
    limit: 5, // get 5 results
    q: 'jones' // query for 'jones'
};
$.ajax({
    url: 'https://data.gov.il/api/3/action/datastore_search',
    data: data,
    dataType: 'jsonp',
    success: function(data) {
        alert('Total results found: ' + data.result.total)
    }
});