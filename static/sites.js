
$.getJSON("https://s3-us-west-2.amazonaws.com/vita-static-content-dev/sites.json", function(sites) {
    console.log(sites);
    var template = $('#hidden-site-template').html();
    for (let site of sites) {
        var site_html = $(template).clone();

        $(site_html).find('#address').html(site.address);
        $(site_html).find('#is_open').html(site.is_open.toString());
        $(site_html).find('#availability_status').html(site.availability_status);
        $(site_html).find('#hours').html(site.hours);
        
        $('#sites-list').append(site_html);
        
    }
});
