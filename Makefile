
PROGRAM = multineat
TEST_DIR = .testing

.PHONY: all clean release debug

all: release

debug:
	rm -f $(PROGRAM) && ./waf build_debug && mv build/debug/$(PROGRAM) .

release:
	rm -f $(PROGRAM) && ./waf build_release && mv build/release/$(PROGRAM) .

clean:
	./waf clean_debug clean_release

test:
	echo "No tests written"
	#rm -r $(TEST_DIR) && mkdir -p $(TEST_DIR)
	#./$(PROGRAM) testdata/transactions.csv $(TEST_DIR)/out.csv
	#diff testdata/sessions.csv $(TEST_DIR)/out.csv
