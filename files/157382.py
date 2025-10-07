<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="kkos"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 12:28:33 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLTNJQ0g4UUk7MjU2OC0wNy0xNzsxMTo1NzoxMiBQTTsyNzY4"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLTNJQ0g4UUk7MjU2OC0wNy0xODsxMjoyODozMyBBTTsxOzI4NjQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="num" type="Integer" array="False" size=""/>
            <declare name="end" type="Integer" array="False" size=""/>
            <declare name="currentNumber" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="num"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <while expression="num &lt;= end">
                <assign variable="currentNumber" expression="num"/>
                <output expression="currentNumber" newline="True"/>
                <assign variable="num" expression="currentNumber + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>