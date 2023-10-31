{
  "classNotes": "用于测试Transaction的类",
  "fileName": "test_transaction",
  "className": "TestCase",
  "import": [
    {
      "type": "request",
      "file": "transaction_docredit_req_page",
      "class": "DoCreditReqPage"
    },
    {
      "type": "response",
      "file": "transaction_docredit_rsp_page",
      "class": "DoCreditRspPage"
    }
  ],
  wwewe wewewe
  
  事实上
  
  "methods":[
  {
    "methodIndex": "1",
    "methodNotes": "此Case用于测试Docredit Sale交易，Amount=200，ecrReferenceNumber=2",
    "requestPageOperations":[
      {
        "pageOperationNote": "选择transaction界面",
        "pageName": "SelectTabPage",
        "pageOperations": [
          {
            "type": "click",
            "name": "click_tab"
          },
          {
            "type": "click",
            "name": "click_transaction"
          }
        ]
      },
      {
        "pageOperationNote": "点击一下顶部的Request，保证切换到Request界面",
        "pageName": "SwitchReqOrRsp",
        "pageOperations": [
          {
            "type": "click",
            "name": "select_req"
          }
        ]
      },
      {
        "pageOperationNote": "做DoCredit交易",
        "pageName": "DoCreditReqPage",
        "pageOperations": [
          {
            "type": "click",
            "name": "click_transactioncommand"
          },
          {
            "type": "click",
            "name": "click_transactioncommand_docreditrequest"
          },
          {
            "type": "click",
            "name": "click_transactiontype"
          },
          {
            "type": "click",
            "name": "click_transactiontype_sale"
          },
          {
            "type": "input",
            "name": "input_amountinformation_transactionamount",
            "value": "200"
          },
          {
            "type": "input",
            "name": "input_traceinformation_ecrreferencenumber",
            "value": "2"
          }
        ]
      },
      {
        "pageOperationNote": "点击开始按钮",
        "pageName": "StartStopPage",
        "pageOperations": [
          {
            "type": "click",
            "name": "start",
            "sleep": 10
          }
        ]
      }
    ],
    "responsePageOperations": [
      {
        "pageOperationNote": "获取响应数据，保存到变量中",
        "pageName": "DoCreditRspPage",
        "variableName": "docreditpage_rsp",
        "pageOperations": [
          {
            "valueName": "response_code",
            "defName": "getvalue_responsecode"
          },
          {
            "valueName": "response_message",
            "defName": "getvalue_responsemessage"
          }
        ]
      }
    ],
    "asserts": {
      "notes": "断言 第一个参数是预期值 第二个是实际值。 如果没达到预期 则抛出错误,是预期值则通过",
      "list_expect": [
        "000000",
        "OK"
      ],
      "list_actual": [
        "response_code",
        "response_message"
      ]
    }
  }
]
}
