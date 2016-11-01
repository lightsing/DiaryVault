myVault:
	@zip -q -R -9 myVault '*.py'
	@echo '#!/usr/bin/env python3' | cat - myVault.zip > myVault
	@chmod +x myVault
	@rm myVault.zip
	@echo "Completed"

.PHONY : clean
clean:
	rm myVault*
