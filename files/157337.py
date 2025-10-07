<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.3"/>
        <attribute name="authors" value="USER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 10:24:16 PM"/>
        <attribute name="created" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0yMjsxMDoxNDozNSBQTTsyNjYz"/>
        <attribute name="edited" value="VVNFUjtERVNLVE9QLVFRVjk1QTA7MjU2OC0wNy0yMjsxMDoyNDoxNiBQTTsxOzI3NzE="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="st, sp" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="st"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="sp"/>
            <while expression="st &lt;= sp">
                <output expression="st" newline="True"/>
                <assign variable="st" expression="st+1"/>
            </while>
        </body>
    </function>
</flowgorithm>