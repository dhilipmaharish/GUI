let inputvalue_dict;

function myFunc(value) {
    console.log(value);
    inputvalue_dict = value
}



function filteremission() {
    $("#emission_type").empty();
    $("#emission_type").append("<option value='' selected disabled>Select</option>");
    inputvalue_dict["emission_filter"][$("#engine_type").val()].forEach(value =>{
        let optionTemplate = `<option value="${value}" >${value}</option>`
        $("#emission_type").append(optionTemplate);
    });

}

function filterAxleLayout() {
    $("#axle_layout_type").empty();
    $("#axle_layout_type").append("<option value='' selected disabled>Select</option>");

    $("#ratio_type").empty();
    $("#ratio_type").append("<option value='' selected disabled>Select</option>");
    
    $("#efficiency_type").empty();
    $("#efficiency_type").append("<option value='' selected disabled>Select</option>");
    inputvalue_dict["axleObject"][$("#axel_type").val()].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`
        $("#axle_layout_type").append(optionTemplate);
    });
}

function filterRatio() {
    $("#ratio_type").empty();
    $("#ratio_type").append("<option value='' selected disabled>Select</option>");

    $("#efficiency_type").empty();
    $("#efficiency_type").append("<option value='' selected disabled>Select</option>");

    let axle_ratio_string = `${$("#axel_type").val()} ${$("#axle_layout_type").val()}`
    inputvalue_dict["axleRatioObject"][axle_ratio_string].forEach(value => {
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#ratio_type").append(optionTemplate);
    });
}

function filterEfficiency(){
    $("#efficiency_type").empty();
    $("#efficiency_type").append("<option value='' selected disabled>Select</option>");
    let axle_efficiency_string = `${$('#axel_type').val()} ${$("#axle_layout_type").val()} ${$("#ratio_type").val()}`
    inputvalue_dict["axelefficiencyObject"][axle_efficiency_string].forEach(value => {
        let optionTemplate = `<option value="${value}">${value}</option>`;
        $("#efficiency_type").append(optionTemplate);
    });
}


function filterstandard(){
    $("#standard_type").empty();
    $("#standard_type").append("<option value='' selected disabled>Select</option>");
    $("#application_type").empty();
    $("#application_type").append("<option value='' selected disabled>Select</option>");
    $("#radius_type").empty();
    $("#radius_type").append("<option value='' selected disabled>Select</option>");
    $("#rrc_type").empty();
    $("#rrc_type").append("<option value='' selected disabled>Select</option>");

    inputvalue_dict["standardObject"][$("#tyre_type").val()].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#standard_type").append(optionTemplate);
    });
    $("#Tyre_details").show();
    if ($("#tyre_type").val() in inputvalue_dict['tire_description_dict']){
        $("#pattern").val(inputvalue_dict['tire_description_dict'][$("#tyre_type").val()]["Pattern"])
        $("#remark").val(inputvalue_dict['tire_description_dict'][$("#tyre_type").val()]["remark"])
    };

}
function filterapplication(){
    $("#application_type").empty();
    $("#application_type").append("<option value='' selected disabled>Select</option>");
    $("#radius_type").empty();
    $("#radius_type").append("<option value='' selected disabled>Select</option>");
    $("#rrc_type").empty();
    $("#rrc_type").append("<option value='' selected disabled>Select</option>");

    let app_string = `${$("#tyre_type").val()} ${$("#standard_type").val()}`
    inputvalue_dict["applicationObject"][app_string].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#application_type").append(optionTemplate);
    });
   
}

function filterradius(){
    $("#radius_type").empty();
    $("#radius_type").append("<option value='' selected disabled>Select</option>");
    $("#rrc_type").empty();
    $("#rrc_type").append("<option value='' selected disabled>Select</option>");

    let app_string = `${$("#tyre_type").val()} ${$("#standard_type").val()} ${$("#application_type").val()}`
    inputvalue_dict['radiusObject'][app_string].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#radius_type").append(optionTemplate);

});
}

function filterrrc(){
    $("#rrc_type").empty();
    $("#rrc_type").append("<option value='' selected disabled>Select</option>");
    let rrc_string = `${$("#tyre_type").val()} ${$("#standard_type").val()} ${$("#application_type").val()} ${$("#radius_type").val()}`
    inputvalue_dict['rrcObject'][rrc_string].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#rrc_type").append(optionTemplate);
    });
   

}

function filtercab(){
    $("#cab").empty();
    $("#cab").append("<option value='' selected disabled>Select</option>");
    $("#rear_body").empty();
    $("#rear_body").append("<option value='' selected disabled>Select</option>");
    $("#air_resistance_type").empty();
    $("#air_resistance_type").append("<option value='' selected disabled>Select</option>");
    inputvalue_dict["vehicle_category_drop"][$("#category").val()].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#cab").append(optionTemplate);
    });
   
}

function filter_rearbody(){
    $("#rear_body").empty();
    $("#rear_body").append("<option value='' selected disabled>Select</option>");
    $("#air_resistance_type").empty();
    $("#air_resistance_type").append("<option value='' selected disabled>Select</option>");
    let app_string = `${$("#category").val()} ${$("#cab").val()}`
    inputvalue_dict["rear_body_drop"][app_string].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#rear_body").append(optionTemplate);
    });
   
}
function filterairresistance(){
    $("#air_resistance_type").empty();
    $("#air_resistance_type").append("<option value='' selected disabled>Select</option>");
    let app_string = `${$("#category").val()} ${$("#cab").val()} ${$("#rear_body").val()}`
    inputvalue_dict["air_drop"][app_string].forEach(value => {            
        let optionTemplate = `<option value="${value}" >${value}</option>`;
        $("#air_resistance_type").append(optionTemplate);
    });
   
}

function loading(){
   
    let all_input = []
    let input = document.querySelectorAll("input");
    let select = document.querySelectorAll("select");
    input.forEach(function(i){
        all_input.push(i.value);
    })
    select.forEach(function(i){
        all_input.push(i.value);
    })
    
    if (all_input.includes('') ){
        $("#content").show()
        
    }
    else{
        $("#loading").show()
        // $("#content").show()
        
    };
    $("#table_display").show()
}

function getgearno(gear_dict){
    $("#Geardiv").show()
    if($("#transmission_type").val() in gear_dict){
        $("#gear_display").val(gear_dict[$("#transmission_type").val()])
    };
};


function uppercase(){
        var x = document.getElementById("Torque_cut");
        x.value = x.value.toUpperCase();      
}


function output_mesage(){
    $("#result").show()
}

function page_load() {
    window.location.href = "http://127.0.0.1:5050/";
  }

