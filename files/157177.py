<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="loop_test4"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:37:53 PM"/>
        <attribute name="created" value="QWRtaW47TEFQVE9QLUJLNFRIREpIOzI1NjgtMDctMTY7MDY6Mjk6NTIgUE07Mjg2NA=="/>
        <attribute name="edited" value="QWRtaW47TEFQVE9QLUJLNFRIREpIOzI1NjgtMDctMTY7MDY6Mzc6NTMgUE07MjsyOTcz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="numStart" type="Integer" array="False" size=""/>
            <declare name="numEnd" type="Integer" array="False" size=""/>
            <output expression="&quot; Input start number: &quot;" newline="True"/>
            <input variable="numStart"/>
            <output expression="&quot; Input end number: &quot;" newline="True"/>
            <input variable="numEnd"/>
            <while expression="numStart &lt;= numEnd">
                <output expression="numStart" newline="True"/>
                <assign variable="numStart" expression="numStart + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>