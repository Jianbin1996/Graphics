module LaneToRasterConverter (
    input logic clk,
    input logic reset,
    input logic [7:0] lane_data [0:WIDTH-1][0:HEIGHT-1],
    output logic [23:0] raster_data [0:WIDTH-1][0:HEIGHT-1]
);

    parameter WIDTH = 640;  // Example width
    parameter HEIGHT = 480; // Example height
    parameter LANE_COLOR = 24'hFF0000; // Red as an example
    parameter BACKGROUND_COLOR = 24'h000000; // Black as background

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            for (int y = 0; y < HEIGHT; y++) begin
                for (int x = 0; x < WIDTH; x++) begin
                    raster_data[x][y] <= BACKGROUND_COLOR;
                end
            end
        end else begin
            for (int y = 0; y < HEIGHT; y++) begin
                for (int x = 0; x < WIDTH; x++) begin
                    if (lane_data[x][y] == 8'hFF) begin  // Assuming 0xFF represents lane pixel
                        raster_data[x][y] <= LANE_COLOR;
                    end else begin
                        raster_data[x][y] <= BACKGROUND_COLOR;
                    end
                end
            end
        end
    end

endmodule