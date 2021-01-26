import json

import pytest

from ssllabs.api.root_certs_raw import RootCertsRaw


class TestRootCertsRaw:

    @pytest.mark.asyncio
    async def test_root_certs_raw(self, request, patch_httpx):
        patch_httpx.return_value._text = json.dumps(request.cls.root_certs)
        r = RootCertsRaw()
        root_certs = await r.get()
        assert type(root_certs) is str
