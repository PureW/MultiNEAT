
LIBRARY = libmultineat.a
PROGRAM = multineat_main
TEST_DIR = .testing

.PHONY: all clean release debug

all: release

debug:
	rm -f build/$(PROGRAM) build/$(LIBRARY) && ./waf build_debug && cp build/debug/$(PROGRAM) build/debug/$(LIBRARY) build/

release:
	rm -f build/$(PROGRAM) build/$(LIBRARY) && ./waf build_release && cp build/release/$(PROGRAM) build/release/$(LIBRARY) build/

clean:
	./waf clean_debug clean_release

test:
	echo "No tests written"
	#rm -r $(TEST_DIR) && mkdir -p $(TEST_DIR)
	#./$(PROGRAM) testdata/transactions.csv $(TEST_DIR)/out.csv
	#diff testdata/sessions.csv $(TEST_DIR)/out.csv
