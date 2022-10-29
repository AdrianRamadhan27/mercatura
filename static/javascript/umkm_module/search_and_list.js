$(document).ready(function(){
    $.getJSON("/umkm/json/", function(data) {
        console.log(data);
        var grid = [];
        $.each(data, function(index, value) {
            var cards = [];
            var content = [];
            content.push("<div class='flex'><img class='w-20 h-20 rounded-full mr-2' src="+ value.fields.logo_usaha+">")
            content.push(`
                <div class="mb-8"> 
                    <div class="font-poppins font-bold text-xl mb-2"><a class="text-purple-1 hover:text-purple-2 no-underline" href="/umkm/detail/`+value.pk+`">` + 
                        value.fields.nama_usaha +
                    `</a></div>
                    <span class="font-poppins inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">` +
                        value.fields.bidang_usaha+
                    `</span>
                    
                    <div class="">
                        <p class="font-poppins text-sm font-semibold text-green mr-2 mb-2 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#00F0B5" class="w-5 h-5">
                        <path fill-rule="evenodd" d="M9.69 18.933l.003.001C9.89 19.02 10 19 10 19s.11.02.308-.066l.002-.001.006-.003.018-.008a5.741 5.741 0 00.281-.14c.186-.096.446-.24.757-.433.62-.384 1.445-.966 2.274-1.765C15.302 14.988 17 12.493 17 9A7 7 0 103 9c0 3.492 1.698 5.988 3.355 7.584a13.731 13.731 0 002.273 1.765 11.842 11.842 0 00.976.544l.062.029.018.008.006.003zM10 11.25a2.25 2.25 0 100-4.5 2.25 2.25 0 000 4.5z" clip-rule="evenodd" />
                        </svg>` +
                            value.fields.lokasi_usaha+
                        `</p>
                    </div>
                </div>
            </div>
            `);
            cards.push(`
                <div class="shadow-md w-full" id="umkm-`+ value.pk +`">
                    <div class="h-20 lg:h-auto lg:w-48 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden"></div>
                    <div class="border-r border-b border-l border-gray-400 lg:border-l lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal hover:bg-gray-100 text-white font-bold py-2 px-4">
                ` + content.join("") + 
                `
                    </div>
                </div>       
                `
            );
            grid.push(cards.join(""));
        });

        $("#umkm-cards").html(grid.join(""));
    });
    $("#search-form").submit(function(e){
        e.preventDefault();
        $("#search-btn").prop('disabled', true);
        $("#search-btn").text('Searching...');
        var $form = $(this);
        var serializedData = $form.serialize();
        $.ajax({
            url: "/umkm/search_umkm/",
            type: "POST",
            data: serializedData,
            dataType: 'json',
            success: function (data) {
                $("#search-btn").prop('disabled', false);
                $("#search-btn").text('Search');
                var grid = [];
                
                $.each(data, function(index, value) {
            var cards = [];
            var content = [];
            content.push("<div class='flex'><img class='w-20 h-20 rounded-full mr-2' src="+ value.fields.logo_usaha+">")
            content.push(`
                <div class="mb-8"> 
                    <div class="font-poppins font-bold text-xl mb-2"><a class="text-purple-1 hover:text-purple-2 no-underline" href="/umkm/detail/`+value.pk+`">` + 
                        value.fields.nama_usaha +
                    `</a></div>
                    <span class="font-poppins inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">` +
                        value.fields.bidang_usaha+
                    `</span>
                    
                    <div class="">
                        <p class="font-poppins text-sm font-semibold text-green mr-2 mb-2 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#00F0B5" class="w-5 h-5">
                        <path fill-rule="evenodd" d="M9.69 18.933l.003.001C9.89 19.02 10 19 10 19s.11.02.308-.066l.002-.001.006-.003.018-.008a5.741 5.741 0 00.281-.14c.186-.096.446-.24.757-.433.62-.384 1.445-.966 2.274-1.765C15.302 14.988 17 12.493 17 9A7 7 0 103 9c0 3.492 1.698 5.988 3.355 7.584a13.731 13.731 0 002.273 1.765 11.842 11.842 0 00.976.544l.062.029.018.008.006.003zM10 11.25a2.25 2.25 0 100-4.5 2.25 2.25 0 000 4.5z" clip-rule="evenodd" />
                        </svg>` +
                            value.fields.lokasi_usaha+
                        `</p>
                    </div>
                </div>
                </div>
            `);
            cards.push(`
                <div class="shadow-md w-full" id="umkm-`+ value.pk +`">
                    <div class="h-20 lg:h-auto lg:w-48 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden"></div>
                    <div class="border-r border-b border-l border-gray-400 lg:border-l lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal hover:bg-gray-100 text-white font-bold py-2 px-4">
                ` + content.join("") + 
                `
                    </div>
                </div>       
                `
            );
            grid.push(cards.join(""));
        });
                if (grid.length == 0) {
                    $("#umkm-cards").html("<h2 class='font-poppins text-purple-1 col-span-4'>Usaha yang dicari tidak ditemukan</h2>");
                } else {
                    $("#umkm-cards").html(grid.join(""));
                }
                
            }
        });
    });
});  