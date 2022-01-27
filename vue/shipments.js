const shipments = {
    template: `
    <div>
    <div class="text-center">
    <label for="start">Start date:</label>
    <input type="text" onfocus="(this.type='date')" onblur="(this.type='text')" id="start" placeholder="Select Start Date" min="2021-05-01" max="2021-08-31" default="2021-05-01" @change="refreshData">
    <label for="end">End date:</label>
    <input type="text" onfocus="(this.type='date')" onblur="(this.type='text')" id="end" placeholder="Select End Date" min="2021-05-01" max="2021-08-31" @change="refreshData">
    </div>
    <table class="table table-striped">
    <thead>
        <tr>
            <th>Shipment ID</th>
            <th>Weight (kg)</th>
            <th>Distance (km)</th>
            <th>Pickup Time</th>
            <th>Drop Off Time</th>
            <th colspan="3">CO2 Emission</th>
        </tr>
        <tr>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th>default</th>
        <th>modeled</th>
        <th>primary</th>
      </tr>
    </thead>
    <tbody>
        <tr v-for="shipment in shipments">
            <td>{{shipment.shipment_id}}</td>
            <td>{{shipment.weight_kg}}</td>
            <td>{{shipment.distance_km}}</td>
            <td>{{shipment.pickup_time}}</td>
            <td>{{shipment.dropoff_time}}</td>
            <td>{{shipment.co2_default}}</td>
            <td>{{shipment.co2_modeled}}</td>
            <td>{{shipment.co2_primary}}</td>
        </tr>
    </tbody>
    </table>
    </div>
    `,
    data(){
        return{
            shipments:[]
        }
    },
    methods:{
        refreshData(){
            start = $("#start").val();
            end = $("#end").val();
            if(start && end){
                // Show Loading Spinner
                $("#spinner").css("display", "block");
                
                axios.get(`http:localhost:8000/shipment?start=${start}&end=${end}`)
                .then((response) => {
                    $("#spinner").css("display", "none");
                    if(response.data.length > 0){
                        this.shipments = response.data;
                    }
                    else {
                        this.shipments = response.data;
                        alert("No entries for selected date range.");
                    }
                });
            }
            
        }
    },
    mounted: function(){
        this.refreshData();
    }
    
}