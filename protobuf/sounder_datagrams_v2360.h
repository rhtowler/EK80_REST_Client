#pragma once

#pragma pack(1)

typedef signed char			int8;
typedef signed short		int16;
typedef signed long			int32;
typedef signed long long	int64;

typedef unsigned char		uint8;
typedef unsigned short		uint16;
typedef unsigned long		uint32;
typedef unsigned long long  uint64;

typedef double				float64;
typedef float				float32;


const uint16 bottom_detection_datagram_id = 301;  // different version, so change the ID
const uint16 integration_datagram_id = 401;  // different version, so change the ID
const uint16 ts_detection_datagram_id = 402;  // different version, so change the ID
const uint16 noise_spectrum_datagram_id = 403;  // different version, so change the ID
const uint16 echogram_datagram_id = 404;  // different version, so change the ID
const uint16 adcp_velocity_datagram_id = 405;  // different version, so change the ID
const uint16 ts_detection_chirp_datagram_id = 406;  // different version, so change the ID
const uint16 adcp_beam_data_datagram_id = 407;  // different version, so change the ID
const uint16 adcp_bottom_detector_datagram_id = 408;  // different version, so change the ID
const uint16 adcp_quality_datagram_id = 409;  // different version, so change the ID
const uint16 adcp_output_datagram_id = 410;  // different version, so change the ID
const uint16 sample_data_datagram_id = 411;  // different version, so change the ID

const uint16 test_datagram_id = 10401;  // different version, so change the ID

// consider common header for all datagrams
// endian, timestamp, encryption, ...

struct bottom_detection_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram

	uint32  ping_number; //?? remove
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601

	char   data_source[60];
	
	float64 bottom_depth;
	float64 reflectivity;
	float64 vessel_log_distance;
	float64 transducer_depth; // remove??
	int32    quality_flag;   // remove??        // -2 Bottom = 0.0,-1 Bottom = syntetic depth ,0 Bottom = ordinary bottom depth
};

struct ts_detection_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram

	uint32  ping_number;
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601

	char   data_source[60];

	//float64 bottom_depth;
	//float64 reflectivity;
	//float64 vessel_log_distance;
	//float64 transducer_depth;
	//int32    quality_flag;           // -2 Bottom = 0.0,-1 Bottom = syntetic depth ,0 Bottom = ordinary bottom depth
};


#if 0

// From EK80 interface spec

struct StructTSDataHeader
{
	DWORDLONG dlTime;
};
struct StructEchoTrace
{
	double Depth; // (m) This is the depth of the target.
	double TSComp; // (dB) This is the compensated Target Strength(TS) value.
	double TSUncomp; // (dB) This is the uncompensated Target Strength(TS) value.
	double AlongshipAngle; // (deg) This is the angle offset in the alongship direction.
	double AthwartshipAngle; // (deg) This is the angle offset in the athwartship direction.
	double sa; // In this context the sA value presents the current biomass index.
};
struct StructTSDataBody
{
	WORD NoOfEchoTraces; // This information identifies the number of individual targets(single fish) in the depth layer.
	StructEchoTrace EchoTraceElement[100];
};
struct StructTSData
{
	StructTSDataHeader TSDataHeader;
	StructTSDataBody TSDataBody;
};

#endif

struct noise_spectrum_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram

	uint32  ping_number;
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601

	char   data_source[60];

	//float64 bottom_depth;
	//float64 reflectivity;
	//float64 vessel_log_distance;
	//float64 transducer_depth;
	//int32    quality_flag;           // -2 Bottom = 0.0,-1 Bottom = syntetic depth ,0 Bottom = ordinary bottom depth
};

struct integration_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram

	uint32  ping_number;
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601

	char    data_source[60];
	
	int32   status_value;
	float64 sa;
	float64 distance;
	float32 frequency_limits[2];
	uint32  spectrum_count;
	float32 frequency_spectrum[1]; // Dummy size, actual length given by spectrum_count
};

struct echogram_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram
	uint64  subscription_id;								

	uint32  ping_number;
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601
	int32	number_of_samples;
	float	start_range;
	float	total_range;

	char   data_source[60];
	int16	echogram_data[1];	// Dummy size, actual length given by number_of_samples

	/*int64	start_index;
	int64	total_number_of_samples;
	float	start_range;
	float	total_range;
	float	bottom_depth;
	int32	processing_result;
	repeated int32 data;*/
};

struct ping_start_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram

	uint32  ping_number;
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601
	
	float32 latitude;										// [º] signed decimal degrees, S = neg. value
	float32 longitude;										// [º] signed decimal degrees, W = neg. value
	float32 heading;										// [º]
	float32 course;											// [º]
	float32 speed_over_ground;								// [m/s]
	float32 heave;											// [m]
	float32 pitch;											// [º]
	float32 roll;											// [º]
};


#pragma region adcp
//TODO. Common solution with octopus_datagrams.h?
const auto size_hcs_velocity_type = sizeof(float64);

struct velocity_vector_hcs
{	
	float64 x; float64 y; float64 z;
};

struct adcp_velocity_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram

	uint32  ping_number;
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601
	
	float64 start_range;
	float64 total_range;
	float64 transducer_depth;
	float64 depth_to_bottom[4];
	float64 blanking_zone;
	uint32 cell_size_samples;
	uint32 processing_result;
	bool is_valid_bottom_data;

	uint32  samples_data_last;
	uint32  samples_data_avg;
	velocity_vector_hcs data_last[1]; // dummy size
	velocity_vector_hcs data_avg[1]; // dummy size
};
#pragma endregion

struct test_datagram
{
	uint32  datagram_id;
	uint32  datagram_size;									// [byte] Total size of datagram

	uint32  ping_number;
	uint64  ping_time;										// [100 nanoseconds] since 01.01 1601
	float32 latitude;										// [º] signed decimal degrees, S = neg. value
	float32 longitude;										// [º] signed decimal degrees, W = neg. value
	float32 heading;										// [º]
	float32 course;											// [º]
	float32 speed_over_ground;								// [m/s]
	float32 heave;											// [m]
	float32 pitch;											// [º]
	float32 roll;											// [º]

	uint32 operation_mode;
	uint32 play_state;
	char   ping_config_changes[120];
};


#pragma pack()
